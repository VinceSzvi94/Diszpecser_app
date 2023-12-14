from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diszpecser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email cím')),
                ('password', models.CharField(max_length=128, verbose_name='Jelszó')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Utolsó bejelentkezés')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Név')),
                ('beosztas', models.CharField(blank=True, max_length=50, null=True, verbose_name='Beosztás')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
        ),
        migrations.CreateModel(
            name='Hivas',
            fields=[
                ('hivas_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Hívás ID')),
                ('hivas_kezdete', models.DateTimeField(verbose_name='Hívás kezdete')),
                ('hivas_vege', models.DateTimeField(blank=True, null=True, verbose_name='Hívás vége')),
                ('hivo_telefonszama', models.CharField(max_length=20, verbose_name='Hívó telefonszáma')),
                ('hivo_neve', models.CharField(blank=True, max_length=150, null=True, verbose_name='Hívó neve')),
                ('telepules', models.CharField(blank=True, null=True, max_length=100, verbose_name='Település')),
                ('kozterulet', models.CharField(blank=True, null=True, max_length=100, verbose_name='Közterület')),
                ('hazszam', models.CharField(blank=True, null=True, max_length=20, verbose_name='Házszám')),
                ('eset_leiras', models.CharField(blank=True, null=True, max_length=500, verbose_name='Eset leírása')),
                ('intezkedes_kezdete', models.DateTimeField(verbose_name='Intézkedés kezdete')),
                ('intezkedes_leirasa', models.CharField(blank=True, null=True, max_length=300, verbose_name='Intézkedés leírása')),
                ('fogado_diszpecser', models.ForeignKey(on_delete=models.DO_NOTHING, to='application.Diszpecser', verbose_name='Fogadó diszpécser')),
            ],
        ),
        migrations.CreateModel(
            name='Eset',
            fields=[
                ('esetkod', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='Esetkód')),
                ('esetnev', models.CharField(max_length=60, verbose_name='Esetnév')),
                ('fontossag', models.IntegerField(verbose_name='Fontosság')),
                ('ertesitesi_szint', models.IntegerField(verbose_name='Értesítési szint')),
            ],
        ),
        migrations.CreateModel(
            name='IntezkedettEsetek',
            fields=[
                # ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hivas_id', models.ForeignKey(on_delete=models.CASCADE, to='application.Hivas', verbose_name='Hívás ID')),
                ('esetkod', models.ForeignKey(on_delete=models.DO_NOTHING, to='application.Eset', verbose_name='Esetkód')),
            ],
        ),
    ]