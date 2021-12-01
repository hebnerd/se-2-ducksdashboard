from site_pages.models import Home
from admin_pages.models import *
from django.contrib.auth.models import User

x = Home(
    id=1,
)
x.save()

x = SiteLook(
    id=1,
    navigation_img_size='width: 90%;',
)
x.save()

x = PetSalesOpts(id=1)
x.save()

x = ProductSalesOpts(id=1)
x.save()

x = SiteVisitsOpts(id=1)
x.save()

x = PagesViewedOpts(id=1)
x.save()

x = UsersOpts(id=1)
x.save()

x = DayAndTimeOpts(id=1)
x.save()

print('\n###### Create initial admin account ######')
print('You must create an initial admin account\nto log into <hostname>/users/login/\n')
fname = input('  First Name: ')
lname = input('  Last Name:  ')
mail  = input('  Email:      ')
uname = input('  Username:   ')
pswd  = input('  Password:   ')

new_usr = User.objects.create_user(first_name=fname, last_name=lname, email=mail,
                                    username=uname, password=pswd, is_staff=True)
new_usr.save()

role_valid = False
while not role_valid:
    role = input('What is your role? [P]O, [S]M, [D]ev, [C]lient, [H]acker: ').lower()
    if role == 'p':
        role = 'Product Owner'
        role_valid = True
    elif role == 's':
        role = 'Scrum Master'
        role_valid = True
    elif role == 'd':
        role = 'Developer'
        role_valid = True
    elif role == 'c':
        role = 'Hacker'
        role_valid = True
    else:
        print('Invalid input!')

usr_profile = UserProfile(
    user=new_usr,
    profile_role=role
)
usr_profile.save()