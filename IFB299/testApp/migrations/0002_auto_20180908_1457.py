# Generated by Django 2.1.1 on 2018-09-08 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.IntegerField(db_column='Customer_ID', primary_key=True, serialize=False)),
                ('customer_name', models.CharField(db_column='Customer_Name', max_length=25)),
                ('customer_phone', models.CharField(db_column='Customer_Phone', max_length=30)),
                ('customer_address', models.CharField(db_column='Customer_Address', max_length=35)),
                ('customer_occupation', models.CharField(db_column='Customer_Occupation', max_length=20)),
                ('customer_birthday', models.DateField(db_column='Customer_Birthday')),
                ('customer_gender', models.CharField(db_column='Customer_Gender', max_length=1)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('location_id', models.IntegerField(db_column='Location_ID', primary_key=True, serialize=False)),
                ('store_state', models.CharField(blank=True, db_column='Store_State', max_length=20, null=True)),
                ('store_city', models.CharField(blank=True, db_column='Store_City', max_length=20, null=True)),
                ('store_address', models.CharField(blank=True, db_column='Store_Address', max_length=30, null=True)),
            ],
            options={
                'db_table': 'locations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Makes',
            fields=[
                ('car_make_key', models.IntegerField(db_column='Car_Make_Key', primary_key=True, serialize=False)),
                ('car_make_name', models.CharField(blank=True, db_column='Car_Make_Name', max_length=20, null=True)),
                ('car_model', models.CharField(blank=True, db_column='Car_Model', max_length=25, null=True)),
                ('car_series', models.CharField(blank=True, db_column='Car_Series', max_length=30, null=True)),
            ],
            options={
                'db_table': 'makes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.IntegerField(db_column='Order_ID', primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField(db_column='Customer_ID')),
                ('car_id', models.IntegerField(db_column='Car_ID')),
                ('pickup_store_id', models.IntegerField(db_column='Pickup_Store_ID')),
                ('return_store_id', models.IntegerField(db_column='Return_Store_ID')),
                ('order_create_date_id', models.IntegerField(db_column='Order_Create_Date_ID')),
                ('pickup_date_id', models.IntegerField(db_column='Pickup_Date_ID')),
                ('return_date_id', models.IntegerField(db_column='Return_Date_ID')),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('store_id', models.IntegerField(db_column='Store_ID', primary_key=True, serialize=False)),
                ('store_name', models.CharField(blank=True, db_column='Store_Name', max_length=30, null=True)),
                ('store_phone', models.CharField(blank=True, db_column='Store_Phone', max_length=25, null=True)),
                ('location_id', models.IntegerField(blank=True, db_column='Location_ID', null=True)),
            ],
            options={
                'db_table': 'stores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestappCustomer',
            fields=[
                ('customer_id', models.IntegerField(db_column='Customer_ID', primary_key=True, serialize=False)),
                ('customer_name', models.CharField(db_column='Customer_Name', max_length=25)),
                ('customer_phone', models.CharField(db_column='Customer_Phone', max_length=30)),
                ('customer_address', models.CharField(db_column='Customer_Address', max_length=35)),
                ('customer_occupation', models.CharField(db_column='Customer_Occupation', max_length=20)),
                ('customer_birthday', models.DateField(db_column='Customer_Birthday')),
                ('customer_gender', models.CharField(db_column='Customer_Gender', max_length=1)),
            ],
            options={
                'db_table': 'testapp_customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Times',
            fields=[
                ('time_id', models.IntegerField(db_column='Time_ID', primary_key=True, serialize=False)),
                ('year', models.IntegerField(db_column='Year')),
                ('month', models.IntegerField(db_column='Month')),
                ('day', models.IntegerField(db_column='Day')),
            ],
            options={
                'db_table': 'times',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('car_id', models.IntegerField(db_column='Car_ID', primary_key=True, serialize=False)),
                ('car_make_key', models.IntegerField(blank=True, db_column='Car_Make_Key', null=True)),
                ('car_series_year', models.IntegerField(blank=True, db_column='Car_Series_Year', null=True)),
                ('car_pricenew', models.IntegerField(blank=True, db_column='Car_PriceNew', null=True)),
                ('car_enginesize', models.CharField(blank=True, db_column='Car_EngineSize', max_length=4, null=True)),
                ('car_fuelsystem', models.CharField(blank=True, db_column='Car_FuelSystem', max_length=25, null=True)),
                ('car_tankcapacity', models.CharField(blank=True, db_column='Car_TankCapacity', max_length=6, null=True)),
                ('car_power', models.CharField(blank=True, db_column='Car_Power', max_length=5, null=True)),
                ('car_seatingcapacity', models.IntegerField(blank=True, db_column='Car_SeatingCapacity', null=True)),
                ('car_standardcapacity', models.CharField(blank=True, db_column='Car_StandardCapacity', max_length=5, null=True)),
                ('car_bodytype', models.CharField(blank=True, db_column='Car_BodyType', max_length=15, null=True)),
                ('car_drive', models.CharField(blank=True, db_column='Car_Drive', max_length=3, null=True)),
                ('car_wheelbase', models.CharField(blank=True, db_column='Car_Wheelbase', max_length=6, null=True)),
            ],
            options={
                'db_table': 'vehicles',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]