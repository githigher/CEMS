import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import VForm3 from 'vform3-builds'
import 'element-plus/dist/index.css'
import 'vform3-builds/dist/designer.style.css'  //引入VForm3样式
import App from './App.vue'
import router from './router.js'
import "echarts";
import VueECharts from 'vue-echarts'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'


const app = createApp(App)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
  }
  
app.use(router).use(ElementPlus)
app.use(VForm3)
app.component('v-chart', VueECharts)

app.mount('#app')