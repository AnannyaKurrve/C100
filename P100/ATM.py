class atm(object):
  """
    blueprint for atm
  """

  def __init__(self, users, atmCard, pinNumber):
    self.color = users
    self.company = atmCard
    self.speed_limit = pinNumber

  def CashWithdrawal(self):
    print("7b")

  def BalanceEnquiry(self):
    print("go ahead ask")

blackCard = atm("me", "BTS", "BTS ARMY FOREVER")

print(blackCard.CashWithdrawal())
print(blackCard.BalanceEnquiry())