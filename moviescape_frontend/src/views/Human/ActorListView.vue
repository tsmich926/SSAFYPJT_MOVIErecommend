<template>
    <div>
        <div>
            <p>ActorListView</p>
            <HumanListItems/>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import HumanListItems from '@/components/HumanListItems.vue'

export default {
name:'ActorListView',
components: {HumanListItems},

data() {
    return {
    // actor:'',
    // actors: [],
    };
},

created() {
    const API = 'http://127.0.0.1:8000/'
    axios({
        method:'get',
        url:`${API}/api/v1/actors/`,
    })
    .then((res)=>{
        console.log(res)
        // this.$router.push({name:''})
    })
    .catch((err)=>{
        console.log(err)
        })
    },
    computed:{
        // actors 
    },
};
</script>

<style>

</style>