import {createRouter, createWebHashHistory} from 'vue-router'
import Login from './components/Login.vue'
import Home from './components/Home.vue'
import SubmitApplication from './components/SubmitApplication.vue'
import SubmitList from './components/SubmitList.vue'
import HomePage from './components/HomePage.vue'
import DataVisualization from './components/DataVisualization.vue'
import Deduct from './components/Deduct.vue'
import Examine from './components/Examine.vue'

const router = createRouter({
    history:createWebHashHistory(),
    routes:[
        {
            path:"/",
            component:Login,
        },
        {
            path:"/home",
            component:Home,
            children:[
                {
                    path:"/home/SubmitApplication",
                    component:SubmitApplication,
                },
                {
                    path:"/home/SubmitList",
                    component:SubmitList,
                },
                {
                    path:"/home/HomePage",
                    component:HomePage,
                },
                {
                    path:"/home/DataVisualization",
                    component:DataVisualization,
                },
                {
                    path:"/home/deduct",
                    component:Deduct,
                },
                {
                    path:"/home/examine",
                    component:Examine,
                },
            ]
        }
    ]
})

export default router