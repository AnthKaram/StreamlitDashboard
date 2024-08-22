import asyncio
import logging
import websockets
from datetime import datetime

from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call_result, call
from ocpp.v16.datatypes import SampledValue
from ocpp.v16.enums import Action, RegistrationStatus, RemoteStartStopStatus

logging.basicConfig(level=logging.INFO)
meter_value_power_active_import = SampledValue(
    value='0', context='Sample.Periodic', format=None, measurand='Power.Active.Import', location=None, unit='W')

class ChargePoint(cp):
    @on(Action.BootNotification)
    async def on_boot_notification(self, charge_point_model, charge_point_vendor, **kwargs):
        return call_result.BootNotificationPayload(
            current_time=datetime.utcnow().isoformat(),
            interval=10,
            status=RegistrationStatus.accepted
        )

    async def send_notification(self):
        request = call.RemoteStartTransactionPayload(
            connector_id=1,
            id_tag="test send"
        )
        response = await self.call(request)
        if response.status == RemoteStartStopStatus.accepted:
            print("sent to central system.")

    @on(Action.MeterValues)
    async def on_meterValues(self, **kwargs):
        return call_result.MeterValues(
        )

    @on(Action.Heartbeat)
    def on_heartbeat(self, **kwargs):
        return call_result.HeartbeatPayload(
            current_time=datetime.utcnow().isoformat()
        )


async def on_connect(websocket, path):
    """ For every new charge point that connects, create a ChargePoint
    instance and start listening for messages.
    """
    try:
        requested_protocols = websocket.request_headers[
            'Sec-WebSocket-Protocol']
    except KeyError:
        logging.info("Client hasn't requested any Subprotocol. "
                 "Closing Connection")
        return await websocket.close()

    if websocket.subprotocol:
        logging.info("Protocols Matched: %s", websocket.subprotocol)
    else:
        # In the websockets lib if no subprotocols are supported by the
        # client and the server, it proceeds without a subprotocol,
        # so we have to manually close the connection.
        logging.warning('Protocols Mismatched | Expected Subprotocols: %s,'
                        ' but client supports  %s | Closing connection',
                        websocket.available_subprotocols,
                        requested_protocols)
        return await websocket.close()

    charge_point_id = path.strip('/')
    cp = ChargePoint(charge_point_id, websocket)
    await asyncio.gather(cp.start(),cp.send_notification())


async def main():
    server = await websockets.serve(
        on_connect,
        '192.168.201.124',#ipv4
        443,
        subprotocols=['ocpp1.6']
    ) #port 443
    logging.info("WebSocket Server Started")
    await server.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())