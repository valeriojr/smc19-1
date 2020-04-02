import random

from monitoring.models import Profile, Address, Monitoring


def create_dummy_profiles(count, suspect=False, result='SR', city='Maceió'):
    for i in range(count):
        profile = Profile.objects.create(full_name='Paciente %d' % random.randrange(1000000),
                                         age=random.randrange(100),
                                         birth_date='1970-01-01'
                                         )
        address = Address.objects.create(profile_id=profile.id, city=city, primary=True)
        monitoring = Monitoring.objects.create(profile_id=profile.id, result=result, suspect=suspect)
