import time
from plyer import notification

if __name__=='__main__':
	while True:
		notification.notify(title="drink water",message="Drinking a lot of water (and that means more than 4-6 litres) over a short time can upset the body's sodium balance, and cause a potentially fatal condition called hyponatremia, or water intoxication.",timeout=15)
		time.sleep(15)#time in second
		break
    
