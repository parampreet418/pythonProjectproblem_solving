class User:
	def __init__(self, username, password, credit=0):
		self.username = username
		self.password = password
		self.credit = int(credit)

	def __str__(self):
		return "{} {} {}".format(self.username, self.password, self.credit)

	def __repr__(self):
		return str(self)


class Database:
	def __init__(self):
		self.users = self.read()
		self.admin_password = "1234"

	def save(self, user_given):
		new_list = []
		insert_flag = False
		for user in self.users:
			if(user.username == user_given.username):
				new_list.append(str(user_given))
				insert_flag = True
			else:
				new_list.append(str(user))
		#new_list = [str(user) for user in self.users]

		if(insert_flag is not True):
			new_list.append(str(user_given))

		text = '\n'.join(new_list)
		with open("accounts.ck","w+") as f:
			f.write(text)

	def read(self):
		with open("accounts.ck","r") as f:
			text = f.read()
		lines = text.splitlines()
		return list([User(*line.split()) for line in lines])

	def find_user(self, username):
		for user in self.users:
			if user.username == username:
				return username
		return None

	def print_all(self, password):
		# check for admin password
		if(self.admin_password == password):
			for user in self.users:
				user = User(user.username,user.password, user.credit)
				print(user.__repr__())
		else:
			print("Incorrect Admin password.")

	def get_number_of_users(self, password):
		# check for admin password
		if(self.admin_password == password):
			count = 0
			for user in self.users:
				count+=1
			print(f' Total users :{count}')
		else:
			print("Incorrect Admin password.")

	def get_total_amount_of_credits(self, password):
		# 1. check for admin password
		# 2. define sum = 0
		# 3. loop on all of self.users
		if (self.admin_password == password):
			sum = 0
			for user in self.users:
				sum = sum + user.credit
			print(f'Total amount of credits : {sum}')
		else:
			print("Incorrect Admin password.")


	def user_exists(self, username):
		for user in self.users:
			if(user.username == username):
				print("User Exist")


	def username_matches_password(self, username, password):
		flag = False
		for user in self.users:
			# find the user with that username
			# check username == password
			if(user.username == username and user.password == password):
				flag = True
		if(flag):
			print("User validated Successfully")

	def show_credit_of_user(self, username, password):
		# 1. check user exists
		# 2. check username and password match
		# 3. find the user and show credit
		credit = 0
		for user in self.users:
			if(user.username == username and user.password == password):
				credit = user.credit
		print(f'User credit : {credit}')
		
	def add_user(self, username, password):
		# 1. check user does not exist
		# 2. create a new User(username, password)
		# 3. append the new user to self.users
		# 4. don't forget to save() !
		userExist = False
		for user in self.users:
			if(user.username == username):
				userExist = True
				print('User already exist!')

		if(userExist is not True):
			user = User(username, password)
			print('New user created')
			self.save(user)



	def add_credit_to_user(self, money, username, password):
		userExist = False
		for user in self.users:
			if (user.username == username):
				userExist = True
				user.credit = user.credit + int(money)
				self.save(user)
				print(f' Total credit :{user.credit}')

		if (userExist is not True):
			new_user = User(username, password, money)
			print(f'New User created with given credit')
			self.save(new_user)

	def send_credit_from_user_to_user(self, money, username1, password1, username2):
		userExist = False
		user1Credit = 0
		for user in self.users:
			if (user.username == username1 and user.password == password1):
				if(user.credit != 0 and user.credit >= money):
					user1Credit = user.credit
					user.credit = user.credit - money
					self.save(user)
					print(f'User 1 updated credit : {user.credit}')
				else:
					print('User does not have enough credits')
		if(user1Credit != 0):
			for user2 in self.users:
				if(user2.username == username2):
					user2.credit = user2.credit + user1Credit
					self.save(user2)
					print(f'User 2 updated credit : {user2.credit}')

