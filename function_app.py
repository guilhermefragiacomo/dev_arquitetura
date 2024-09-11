import logging
import azure.functions as func

app = func.FunctionApp()

def HelloWorld():
    print("Hello, World!")

@app.schedule(schedule="0 12 * * THU", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')
        HelloWorld()

    logging.info('Python timer trigger function executed.')