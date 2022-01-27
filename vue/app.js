const routes = [
    {path:"/", component:home},
    {path:"/shipments", component:shipments},
];

const router = new VueRouter({
    routes
})

const app = new Vue({
    router
}).$mount("#app");