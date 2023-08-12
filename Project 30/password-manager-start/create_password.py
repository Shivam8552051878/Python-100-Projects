#Password Generator Project
import random

class PaassworGenerator():
  def __init__(self):
      self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
      self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
      self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

      self.nr_letters = random.randint(8, 10)
      self.nr_symbols = random.randint(2, 4)
      self.nr_numbers = random.randint(2, 4)

  def random_password(self):
      password_list = [self.letters[chr] for chr in range(self.nr_letters)] + [self.numbers[sym] for sym in range(self.nr_symbols)] + [self.symbols[num] for num in range(self.nr_numbers)]
      random.shuffle(password_list)

      password = "".join(password_list)
      print(f"Your password is: {password}")
      return password
# for char in range(nr_letters):
#   password_list.append(random.choice(letters))
#
# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#   password_list += random.choice(numbers)

#
# password = PaassworGenerator()
# password.random_password()
