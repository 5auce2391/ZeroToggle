# app_code.py
def adjust_thermostat(current_temp: int) -> str:
    target_temp = 72
    return f"Thermostat set to {target_temp}°F (Current: {current_temp}°F)"

def trigger_security_alarm() -> str:
    return "🚨 Security System ARMED - Motion Sensors Active"

def turn_on_living_room_lights() -> str:
    return "💡 Living Room Lights turned ON (Brightness: 80%)"

def run_smart_home_routine(temperature: int) -> str:
    status_reports = []
    status_reports.append(adjust_thermostat(temperature))
    status_reports.append(trigger_security_alarm())
    status_reports.append(turn_on_living_room_lights())
    return "\n".join(status_reports)
