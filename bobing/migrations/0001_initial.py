# Generated by Django 2.0.7 on 2018-09-15 17:53

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sysmem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(max_length=100, verbose_name='昵称')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '管理人员',
                'verbose_name_plural': '管理人员',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=100, verbose_name='活动名称')),
                ('is_open', models.BooleanField(default=False, verbose_name='是否启用')),
                ('errmsg', models.CharField(max_length=100, verbose_name='关闭提示')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('times', models.TimeField(verbose_name='每日起')),
                ('timee', models.TimeField(verbose_name='每日止')),
                ('text', models.CharField(max_length=256, verbose_name='备用文本')),
            ],
            options={
                'verbose_name': '活动设置',
                'verbose_name_plural': '活动设置',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('username', models.CharField(max_length=150, verbose_name='会员账号')),
                ('score', models.IntegerField(default=0, verbose_name='抽奖次数')),
                ('extra_int', models.IntegerField(default=0, verbose_name='备用数字')),
                ('extra_str', models.CharField(default=None, max_length=255, verbose_name='备用文字')),
            ],
            options={
                'verbose_name': '抽奖会员',
                'verbose_name_plural': '抽奖会员',
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prize_id', models.IntegerField(default=None, verbose_name='礼品编号')),
                ('name', models.CharField(max_length=150, verbose_name='礼品名称')),
                ('desc', models.CharField(default='', max_length=250, verbose_name='中奖描述')),
                ('probability', models.DecimalField(decimal_places=3, max_digits=8, null=True, verbose_name='中奖概率（0.001%）')),
                ('num', models.IntegerField(default=0, verbose_name='数量')),
                ('is_show', models.BooleanField(default=1, verbose_name='列表显示')),
            ],
            options={
                'verbose_name': '奖品管理',
                'verbose_name_plural': '奖品管理',
            },
        ),
        migrations.CreateModel(
            name='Rec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('send_time', models.DateTimeField(default=None, null=True, verbose_name='发送时间')),
                ('is_sent', models.BooleanField(default=False, verbose_name='是否发送')),
                ('user_ip', models.GenericIPAddressField(verbose_name='抽奖IP')),
                ('way', models.CharField(default='自然抽奖', max_length=100, verbose_name='抽奖方式')),
                ('prize', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bobing.Prize', verbose_name='奖品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bobing.Member', verbose_name='用户')),
            ],
            options={
                'verbose_name': '抽奖记录',
                'verbose_name_plural': '抽奖记录',
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('username', models.CharField(default='', max_length=150, verbose_name='会员账号')),
                ('prize_id', models.IntegerField(default=0, verbose_name='中奖礼品')),
                ('is_use', models.BooleanField(default=False, verbose_name='是否使用')),
                ('use_time', models.DateTimeField(default=None, null=True, verbose_name='使用时间')),
            ],
            options={
                'verbose_name': '内定规则',
                'verbose_name_plural': '内定规则',
            },
        ),
    ]
