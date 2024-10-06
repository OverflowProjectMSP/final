import { createRouter, createWebHistory } from "vue-router";
export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/:pathMatch(.*)*",
      component: () => import("../components/ReuseComponets/ErrorFour.vue"),
    },
    {
      path: "/",
      component: () => import("../components/Main/MainComp.vue"),
    },
    {
      path: "/States",
      component: () => import("../components/States/States.vue"),
    },
    {
      path: "/NewState",
      component: () => import("../components/States/NewState.vue"),
    },
    {
      path: "/StateItem/:id",
      component: () => import("../components/States/StateItem.vue"),
    },
    {
      path: "/Login",
      component: () => import("../components/Login/EnterPage.vue"),
    },
    {
      path: "/SignUp",
      component: () => import("../components/Login/RegisterPage.vue"),
    },
    {
      path: "/RecoveryPassPage",
      component: () => import("../components/Login/RecoveryPassPage.vue"),
    },
    {
      path: "/EnterCodePage",
      component: () => import("../components/Login/EnterCodePage.vue"),
    },
    {
      path: "/EnterCode",
      component: () => import("../components/Login/EnterCodePage1.vue"),
    },
    {
      path: "/EnterNewPassword",
      component: () => import("../components/Login/EnterNewPassword.vue"),
    },
    {
      path: "/FAQ",
      component: () => import("../components/FAQ/FAQ.vue"),
    },
    {
      path: "/Questions",
      component: () => import("../components/Questions/Questions.vue"),
    },
    {
      path: "/NewQuestion",
      component: () => import("../components/Questions/NewQuestion.vue"),
    },
    {
      path: "/Profile/:id",
      component: () => import("../components/Profile/NewProfileComp.vue"),
    },
    {
      path: "/QuestionItem/:id",
      component: () => import("../components/Questions/QuestionItem.vue"),
    },
    // {
    //   path: "/Forum/:lang",
    //   component: () => import("../components/Forum/Forum.vue"),
    // },
    // {
    //   path: "/ForumPage",
    //   component: () => import("../components/Forum/ForumPage.vue"),
    // },
    // {
    //   path: "/ProfileSettings",
    //   component: () => import("../components/Profile/SettingsProfile.vue"),
    // },
    {
      path: "/ChangePassword",
      component: () => import("../components/Profile/ChangePassword.vue"),
    },
    {
      path: "/UpdateQuestion/:id",
      component: () => import("../components/Questions/UpdateQuestion.vue"),
    },
    {
      path: "/UpdateState/:id",
      component: () => import("../components/States/UpdateState.vue"),
    },
    {
      path: "/Test",
      component: () => import("../components/Telegram/DescriptionTg.vue"),
    },
    {
      path: "/auth-tg/:id",
      component: () => import('../components/Telegram/TelegramComp.vue'),
      props: true
    },
    {
      path: "/auth-tg-info",
      component: () => import('../components/Telegram/TelegramInfoComp.vue'),
      props: true
    },
    {
      path: "/auth-tg-desription",
      component: () => import('../components/Telegram/DescriptionTg.vue'),
      props: true
    },
    {
      path: "/leaders",
      component: () => import('../components/Profile/LeadersComp.vue'),
    },
    {
      path: "/edit",
      component: () => import('../components/Edit/NewqueVid.vue')
    },
    {
      path: "/editNewNav",
      component: () => import('../components/ReuseComponets/NewnavBar.vue')
    },
    {
      path: "/uftwo",
      component: () => import('../components/Edit/UfTwo.vue')
    },
    {
      path: "/abouterror",
      component: () => import('../components/Other/AbouterrorComp.vue')
    },
    {
      path: "/pre",
      component: () => import('../components/Preloader2.vue')
    },
    {
      path: "/newsetting",
      component: () => import('../components/Profile/NewsettingComp.vue')
    },
    {
      path: "/NewProfile",
      component: () => import('../components/Profile/NewProfileComp.vue')
    },
    {
      path: "/OfferTheme",   
      component: () => import('../components/Other/OfferComp.vue')
    },
    {
      path: "/Changepass",
      component: () => import('../components/Profile/ChangepassComp.vue')
    },
    {
      path: "/LeaderTable",
      component: () => import('../components/Other/LeadertableComp.vue')
    },
    {
      path: "/Pagination",
      component: () => import('../components/Pagination/PaginationComments.vue')
    },
    
  ],
});
