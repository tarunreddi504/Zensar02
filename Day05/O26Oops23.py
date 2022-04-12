
import O25Oops22

def withDraw(self):
    print("You can withdraw upto 4k per day....")

# monkey patching
O25Oops22.HDFC.withDraw = withDraw

print("-" * 40)
hdfc = O25Oops22.HDFC()
hdfc.withDraw()
