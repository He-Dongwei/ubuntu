from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from artical import models as ar_m
from .conf import settings
from .managers import UserInheritanceManager, UserManager

class company(models.Model):
    companyhead=models.CharField(_('发票抬头'),max_length=255)
    companynumber=models.CharField(_('单位纳税识别号'),max_length=30)
    phone=models.CharField(_('电话'),max_length=11,null=True)
    address=models.CharField(_('地址'),null=True,max_length=255)
    bank=models.CharField(_('开户行'),null=True,max_length=255)
    accountnumber=models.CharField(_('开户账号'),null=True,max_length=30)
    def __str__(self):
        return self.billhead
    class Meta:
        verbose_name=_('发票单位')
        verbose_name_plural = _('发票单位')

class AbstractUser(AbstractBaseUser, PermissionsMixin):
    USERS_AUTO_ACTIVATE = not settings.USERS_VERIFY_EMAIL
    company = models.ForeignKey(company, null=True)
    name = models.CharField(_('用户名'), max_length=30, null=True, unique=True)
    sex = models.CharField(_('性别'), max_length=6, null=True,choices=(('0',_('男')),('1',_('女'))))
    email = models.EmailField(_('邮箱'), max_length=255, unique=True, db_index=True)  # 邮箱
    email2 = models.EmailField(_('备用邮箱'), max_length=255, unique=True, null=True)
    realname = models.CharField(_('姓名'), max_length=30, null=True)
    phonenumber = models.CharField(_('手机号码'), max_length=11, null=True)
    officephone = models.CharField(_('办公电话'), max_length=11, unique=True, null=True)
    job = models.CharField(_('职称'), max_length=30, null=True)
    workunit = models.CharField(_('工作单位'), max_length=255, null=True)
    address = models.CharField(_('通讯地址'), max_length=255, null=True)
    postcode = models.CharField(_('邮编'), max_length=6, null=True)
    is_author = models.BooleanField(_('是否是作者'), default=False)

    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.')) #能进入管理台才能更改

    is_active = models.BooleanField(
        _('active'), default=USERS_AUTO_ACTIVATE,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')) #是否激活
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now) #注册日期
    user_type = models.ForeignKey(ContentType, null=True, editable=False) #用户类型

    objects = UserInheritanceManager()
    base_objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        abstract = True

    def get_full_name(self):
        """ Return the email."""
        return self.email

    def get_short_name(self):
        """ Return the email."""
        return self.email

    def email_user(self, subject, message, from_email=None):
        """ Send an email to this User."""
        send_mail(subject, message, from_email, [self.email])

    def activate(self):
        self.is_active = True
        self.save()

    def save(self, *args, **kwargs):
        if not self.user_type_id:
            self.user_type = ContentType.objects.get_for_model(self, for_concrete_model=False)
        super(AbstractUser, self).save(*args, **kwargs)


class User(AbstractUser):

    """
    Concrete class of AbstractUser.
    Use this if you don't need to extend User.
    """

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name=_('用户')
        verbose_name_plural=_('用户')
class accessrecord(models.Model):
    user = models.CharField(_('浏览人'), max_length=30)
    time=models.DateTimeField(_('访问时间'),auto_now_add=True)
    page=models.URLField(_('访问页面'))
    IP=models.GenericIPAddressField(_('访问IP'))
    comment=models.CharField(_('备注'),max_length=255,null=True)
    def __str__(self):
        return self.user
    class Meta:
        verbose_name=_('上网记录')
        verbose_name_plural=_('上网记录')
class payment(models.Model):
    user=models.ForeignKey(User)
    paper=models.OneToOneField(ar_m.paper)
    paycompany=models.CharField(_('缴费单位名称'),max_length=255)
    paytime=models.DateTimeField(_('缴费时间'))
    paymoney=models.DecimalField(_('缴费金额'),max_digits=8,decimal_places=2)
    payaccount=models.CharField(_('缴费账号'),max_length=30)
    comment=models.CharField(_('备注'),max_length=1000)
    creditfile=models.FileField(_('凭证文件'))
    def __str__(self):
        return self.paycompany
    class Meta:
        verbose_name=_('缴费记录')
        verbose_name_plural=_('缴费记录')

class bill(models.Model):
    payment=models.OneToOneField(payment,null=True)
    company=models.ForeignKey(company,null=True)
    billnumber=models.CharField(_('发票编号'),max_length=50)
    def __str__(self):
        return self.billnumber
    class Meta:
        verbose_name=_('发票')
        verbose_name_plural=_('发票')


#评论
class comment(models.Model):
    #user=models.ForeignKey(User,null=True)
    web=models.ForeignKey(ar_m.web,null=True)
    commentName=models.CharField(_('评论人'),max_length=30)
    commentTime=models.DateTimeField(_('评论时间'),null=True)
    commentLevel=models.CharField(_('评分'),max_length=1,null=True,choices=(('A',_('A')),('B',_('B')),('C',_('C')),('D',_('D')),('E',_('E'))))
    commentReviewer=models.CharField(_('审核人'),max_length=30)
    commentReviewTime=models.DateTimeField(_('审核时间'),null=True)
    reviewStatus=models.CharField(_('审核状态'),max_length=1,null=True,choices=(('0',_('未审核')),('1',_('正在审核')),('2',_('已审核')),('3',_('批准')),('4',_('拒绝'))))
    def __str__(self):
        return self.commentName
    class Meta:
        verbose_name=_('评论')
        verbose_name_plural=_('评论')

