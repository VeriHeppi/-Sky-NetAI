import win32com.client

class CalendarEvent:
    def __init__(self):
        self.outlook = win32com.client.Dispatch("Outlook.Application")

    def create_event(self, subject, start_time, duration):
        appointment = self.outlook.CreateItem(1)  # 1=outlook appointment item
        appointment.Start = start_time
        appointment.Subject = subject
        appointment.Duration = duration
        appointment.Save()
