import sentry_sdk
import time

sentry_sdk.init(
    dsn="",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)

str1=5
noo=2
no=0
while True:
    no=no+1
    print('Test1 Sent2')
    u1=int(input("Enter commmand:"))
    if u1==1:
        time.sleep(3)
        break
    try:
        str1+noo
    except Exception as err:
        sentry_sdk.capture_exception(err)
    try:
        print(''+str(u1))
        print(u1*3)
    except Exception as err:
        sentry_sdk.capture_exception(err)
    try:
        st=str1122()
    except Exception as err:
        sentry_sdk.capture_exception(err)
    
    

