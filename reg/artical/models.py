from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.contenttypes.models import ContentType

# Create your models here.

#论文实体
class paper(models.Model):
    paper_Theme=models.CharField(_('论文主题'),max_length=255,null=True)
    paperChineseName=models.CharField(_('论文中文名称'),max_length=255)
    paperEnglishName=models.CharField(_('论文英文名称'),max_length=255)
    paperChineseSummary=models.TextField(_('论文中文摘要'))
    paperEnglishSummary=models.TextField(_('论文英文摘要'))
    paperFiles=models.FileField(_('论文附件'))
    paperStatus=models.CharField(_('论文录用状态'),null=True,max_length=1,choices=(('0',_('已投稿')),('1',_('审稿')),('2',_('已录用')),('3',_('已拒绝'))))
    def __str__(self):
        return self.paper_Theme
    class Meta:
        verbose_name=_('论文')
        verbose_name_plural=_('论文')
#
#期刊实体
class journal(models.Model):
    jourName=models.CharField(_('期刊名称'),max_length=30)
    jourLevel=models.CharField(_('期刊等级'),null=True,choices=(('A1',_('A1学术期刊')),('A2',_('A2学术期刊')),('B1',_('B1学术期刊')),('B2',_('B2学术期刊')),('C',_('C普通期刊'))),max_length=4)#用编码表示
    jourManager=models.CharField(_('期刊联系人'),max_length=30)
    jourPhone=models.CharField(_('期刊联系手机号'),max_length=11)
    jourOfficePhone=models.CharField(_('期刊办公电话'),max_length=12,null=True)
    jourEmail=models.CharField(_('期刊邮件地址'),max_length=255,null=True)
    jourUrl=models.CharField(_('期刊网址'),max_length=255)
    def __str__(self):
        return self.jourName
    class Meta:
        verbose_name=_('期刊')
        verbose_name_plural=_('期刊')
#n-n

#作者实体
class author(models.Model):
    paper=models.ManyToManyField(paper)
    authorName=models.CharField(_('作者姓名'),max_length=30) 
    authorCompany=models.CharField(_('作者工作单位'),max_length=255,null=True)
    authorAddress=models.CharField(_('作者地址'),max_length=255,null=True)
    authorPhone=models.CharField(_('作者手机号'),max_length=11,null=True)
    authorOfficePhone=models.CharField(_('作者办公电话'),max_length=12,null=True)
    authorEmail=models.CharField(_('作者邮件地址'),max_length=30,null=True)
    authorJob=models.CharField(_('作者职称'),max_length=30,null=True)#用编码表示，是否为学生，学生类型
    def __str__(self):
        return self.authorName
    class Meta:
        verbose_name=_('作者')
        verbose_name_plural=_('作者')
	
	
#审稿专家实体
class reviewer(models.Model):
    paper=models.ManyToManyField(paper,through='review')
    reviewerName=models.CharField(_('姓名'),max_length=30)
    reviewerWorkplace=models.CharField(_('工作单位'),max_length=255)
    reviewerTitle=models.CharField(_('职称'),max_length=3)
    reviewerPhone=models.CharField(_('手机'),max_length=11)
    reviewerOfficePhone=models.CharField(_('办公电话'),max_length=12)
    reviewerEmail=models.CharField(_('邮件地址'),max_length=128)
    reviewerSecondEmail=models.CharField(_('备用邮箱'),max_length=128)
    reviewerBankName=models.CharField(_('银行名称'),max_length=255)
    reviewerBanknumber=models.CharField(_('银行账号'),max_length=30)
    reviewerMoney=models.DecimalField(_('审稿金额'),max_digits=8,decimal_places=2,null=True)
    reviewernumber=models.IntegerField(_('审稿论文数'),null=True)
    def __str__(self):
        return self.reviewerName
    class Meta:
        verbose_name=_('专家')
        verbose_name_plural=_('专家')


#审稿
class review(models.Model):
    paper=models.ForeignKey(paper)
    reviewer=models.ForeignKey(reviewer)
    reviewTime=models.DateTimeField(_('审稿时间'),null=True)
    reviewOpinionToAuthor=models.TextField(_('给作者的审稿意见'),null=True)
    reviewOpinionToEditor=models.TextField(_('给编辑的审稿意见'),null=True)
    reviewResult=models.CharField(_('审稿结果'),max_length=1,null=True,choices=(('0',_('强烈推荐')),('1',_('推荐')),('2',_('弱推荐')),('3',_('弱拒绝')),('4',_('拒绝')),('5',_('强烈拒绝'))))
    def __str__(self):
        return self.reviewer.reviewerName
    class Meta:
        verbose_name=_('审稿')
        verbose_name_plural=_('审稿')
#审稿结果用编码表示


#网页实体
class web(models.Model):
    webTitle=models.CharField(_('网页title'),max_length=255)
    webUrl=models.CharField(_('网址'),max_length=255)
    webDetail=models.TextField(_('网页内容'),null=True)
    webAuthor=models.CharField(_('作者'),max_length=30)
    webCreateTime=models.DateTimeField(_('生成时间'),null=True)
    webModifyTime=models.DateTimeField(_('修改时间'),null=True)
    webModifier=models.CharField(_('修改人'),max_length=30)
    firstReviewer=models.CharField(_('第一审核人'),max_length=30,null=True)
    firstReviewTime=models.DateTimeField(_('一审时间'),null=True)
    firstReviewOpinion=models.TextField(_('一审意见'),null=True)
    firstReviewStatus=models.CharField(_('一审状态'),max_length=1,null=True,choices=(('0',_('未审核')),('1',_('正在审核')),('2',_('已审核')),('3',_('批准')),('4',_('拒绝'))))
    secondReviewer=models.CharField(_('第二审核人'),max_length=30,null=True)
    secondReviewTime=models.DateTimeField(_('二审时间'),null=True)
    secondReviewOpinion=models.TextField(_('二审意见'),null=True)
    secondReviewStatus=models.CharField(_('二审状态'),max_length=1,null=True,choices=(('0',_('未审核')),('1',_('正在审核')),('2',_('已审核')),('3',_('批准')),('4',_('拒绝'))))
    approver=models.CharField(_('批准人'),max_length=30)
    approvalTime=models.DateTimeField(_('批准时间'),null=True)
    approvalOpinion=models.TextField(_('批准意见'),null=True)
    approvalStatus=models.CharField(_('批准状态'),max_length=1,null=True,choices=(('0',_('正在批准')),('1',_('批准')),('2',_('拒绝'))))
    def __str__(self):
        return self.webTitle
    class Meta:
        verbose_name=_('网页')
        verbose_name_plural=_('网页')


