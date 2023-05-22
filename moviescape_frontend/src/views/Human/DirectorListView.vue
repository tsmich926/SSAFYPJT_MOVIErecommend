<template>
    <div>
        <div>
            <p>DirectorListView</p>
            <HumanListItems :ITEMhumans="director_list"/>
        </div>
        <infinite-loading @infinite="getWholeDirectors"></infinite-loading>
    </div>
</template>

<script>
import InfiniteLoading from 'vue-infinite-loading'
import axios from 'axios';
import HumanListItems from '@/components/HumanListItems.vue'

export default {
    name:'DirectorListView',
    components: {
        HumanListItems,
        InfiniteLoading
    },

    data() {
        return {
            page:0,
            directors: [],
        };
    },
    computed:{
        director_list (){
            return this.directors
        }
    },
    methods: {
        getWholeDirectors($state){
            axios({
                method:'get',
                url:`http://127.0.0.1:8000/api/v1/directors/`,
                params:{
                    page:this.page
                }
            })
            .then((res)=>{
                console.log(res)
                if (res.data.length){
                    this.page+=1
                    this.directors.push(...res.data)
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
};
</script>

<style>

</style>