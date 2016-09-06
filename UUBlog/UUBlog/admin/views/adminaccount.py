#-*- coding:utf-8 -*-


from django.contrib import auth
from django.contrib.auth.models import User

from UUBlog.common import pub
from UUBlog.models import UserProfile
from UUBlog.uu.ubaseblog import  UBaseBlogView
from UUBlog.uu.ubaseadmin import UBaseAdminView



class RegisterView(UBaseBlogView):
    def DefaultTemplateName(self):
        return "register"

    def GetContext(self, **kwargs):
        uid = int(kwargs.get("uid", 0))

        return locals()

    def PostContext(self, **kwargs):
        uid = int(kwargs.get("uid", 0))

        if self.HasPostData("ok"):
            username = self.GetPostData("username")
            password = self.GetPostData("password")
            email = self.GetPostData("email")

            user = User.objects.create_user(username, email, password)
            user.first_name = username
            user.save()

            profile = UserProfile(user=user)
            profile.nickname = user.username
            profile.save()

        self.redirectUrl = "/"

        return locals()

class LoginView(UBaseBlogView):
    def GetContext(self, **kwargs):
        self.SetTemplateName("admin/login.html")
        return locals()

    def PostContext(self, **kwargs):

        if self.HasPostData("ok"):
            username=self.GetPostData("username")
            password=self.GetPostData("password")

            user=auth.authenticate(username=username,password=password)
            if user is not None:
                #userProfile=user.get_profile()
                
                #try:
                #    blog=Blog.objects.get(id=user.id)
                #except:
                #    pass
                  
                if user.is_active:
                    auth.login(self.request,user)

        self.redirectUrl="/admin/"

        return locals()

class LogoutView(UBaseBlogView):
    def GetContext(self, **kwargs):

        auth.logout(self.request)
        self.redirectUrl="/"

        return locals()

#头像
class AvatarView(UBaseAdminView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        self.template_name="accounts/pub/avatar.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))
        #000/00/01
        if self.HasPostData("ok") and self.request.FILES['avatar']:
            avatarPath=("%d" %self.currentUserProfile.user_id).rjust(7,"0")
            dir1=avatarPath[0:3]
            dir2=avatarPath[3:5]
            fileName=avatarPath[5:7]
            path="%s/%s/%s/" %("avatar",dir1,dir2)

            self.currentUserProfile.avatar=pub.SaveFile(self.request.FILES['avatar'],path,fileName)[0]
      
            self.currentUserProfile.save()

        return locals()

#基本信息
class BaseView(UBaseAdminView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        self.template_name="accounts/pub/base.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
            self.currentUserProfile.nickname=self.GetPostData("nickname")
            self.currentUserProfile.realname=self.GetPostData("realname")
            self.currentUserProfile.gender=self.GetPostData("gender")
            self.currentUserProfile.birthday=self.GetPostData("birthday")
            self.currentUserProfile.birthcity=self.GetPostData("birthcity")
            self.currentUserProfile.residecity=self.GetPostData("residecity")
      
            self.currentUserProfile.save()

        return locals()

#个人信息
class InfoView(UBaseAdminView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        self.template_name="accounts/pub/info.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
            self.currentUserProfile.affectivestatus=self.GetPostData("affectivestatus")
            self.currentUserProfile.lookingfor=self.GetPostData("lookingfor")
            self.currentUserProfile.bloodtype=self.GetPostData("bloodtype")
            self.currentUserProfile.site=self.GetPostData("site")
            self.currentUserProfile.bio=self.GetPostData("bio")
            self.currentUserProfile.interest=self.GetPostData("interest")
            self.currentUserProfile.sightml=self.GetPostData("sightml")
            self.currentUserProfile.timeoffset=self.GetPostData("timeoffset")

            self.currentUserProfile.save()

        return locals()

#联系方式
class ContactView(UBaseAdminView):
    def GetContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        self.template_name="accounts/pub/contact.html"

        return locals()

    def PostContext(self, **kwargs):
        uid=int(kwargs.get("uid",0))

        if self.HasPostData("ok"):
            self.currentUserProfile.qq=self.GetPostData("qq")
            self.currentUserProfile.msn=self.GetPostData("msn")
            self.currentUserProfile.taobao=self.GetPostData("taobao")
            self.currentUserProfile.email=self.GetPostData("email")
            self.currentUserProfile.phone=self.GetPostData("phone")
            self.currentUserProfile.mobile=self.GetPostData("mobile")
            self.currentUserProfile.address=self.GetPostData("address")
            self.currentUserProfile.zipcode=self.GetPostData("zipcode")

            self.currentUserProfile.save()

        return locals()

from django.contrib import messages
#安全
class SecurityView(UBaseAdminView):
    def DefaultTemplateName(self):
        return "account/security"

    def GetContext(self, **kwargs):
        self.message = self.GetCookie("changedpasswordsuccess", None)
        return locals()

    def GetResponse(self, response):
        return super(SecurityView, self).GetResponse(response)

    def PostContext(self, **kwargs):

        if self.HasPostData("ok"):
            oldpassword = self.GetPostData("oldpassword")
            newpassword1 = self.GetPostData("newpassword1")
            newpassword2 = self.GetPostData("newpassword2")

            user = auth.authenticate(username=self.user.username,password=oldpassword)
            if user is None:
                self.message = "旧密码不正确"
                return locals()
            else:
                if newpassword1 == "" or newpassword1 != newpassword2:
                    self.message = "两次密码不一致"
                    return locals()
                else:
                    user.set_password(newpassword1)
                    self.reload = True
                    self.SetCookie("changedpasswordsuccess","修改密码成功")
                    return locals()

        return locals()



    def PostResponse(self, response):
        response.set_cookie("aaa","bbb")
        return response


def UsersMeta(request,uid):
    ret={}
    isMe=False
    currentUser=None
    if request:
        currentUser=request.user
        uid=int(uid)

        if not currentUser or not currentUser.id:
            currentUser=None
         
        if currentUser and currentUser.id==uid:
            isMe=True

    ret.setdefault("isme",isMe)
    ret.setdefault("currentuser",currentUser)

    if uid>0:
        try:
            isGuest=True
            guestUser=User.objects.get(id=uid)
        except:
            isGuest=False
            guestUser=None
    else:
        isGuest=False
        guestUser=None

    ret.setdefault("isguest",isGuest)
    ret.setdefault("guestuser",guestUser)
    # user end

    #userprofile begin
    currentUserProfile=None
    if  currentUser:
        try:
            currentUserProfile=currentUser.get_profile()
        except:
            #createUserProfile(currentUser)
            #currentUserProfile=currentUser.get_profile()
            currentUserProfile=None
    ret.setdefault("currentuserprofile",currentUserProfile)

    guestUserProfile=None
    if guestUser:
        try:
            guestUserProfile=guestUser.get_profile()
        except:
            #createUserProfile(guestUser)
            #guestUserProfile=guestUser.get_profile()
            guestUserProfile=None
    ret.setdefault("guestuserprofile",guestUserProfile)
    #userprofile end

   



    return ret