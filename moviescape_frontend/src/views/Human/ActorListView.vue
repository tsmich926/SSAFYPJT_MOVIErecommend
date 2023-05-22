<template>
    <div>
        <div>
            <p>ActorListView</p>
            <HumanListItems :ITEMhumans="actor_list"/>
        </div>
        <infinite-loading @infinite="getWholeActors"></infinite-loading>
    </div>
</template>

<script>
import InfiniteLoading from 'vue-infinite-loading'
import axios from 'axios'
import HumanListItems from '@/components/HumanListItems.vue'

export default {
    name:'ActorListView',
    components: {
        HumanListItems,
        InfiniteLoading
    },
    data() {
        return {
            page:0,
            actors: [],
        };
    },
    computed:{
        actor_list (){
            return this.actors
        }
    },
    methods: {
        getWholeActors($state){
            axios({
                method:'get',
                url:`http://127.0.0.1:8000/api/v1/actors/`,
                params:{
                    page:this.page
                },
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                }
            })
            .then((res)=>{
                console.log(res)
                if (res.data.length){
                    this.page+=1
                    this.actors.push(...res.data)
                    $state.loaded();
                }else{
                    $state.complete()
                }
            })
            .catch((err)=>{
                console.log(err)
            })
        }
    },
    created(){
        this.getWholeActors()
    }   
};

</script>

<style>

</style>