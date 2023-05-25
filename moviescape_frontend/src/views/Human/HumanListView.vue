<template>
    <div class= "my_MovieListView_BGC">
        <h1 style="margin-bottom:50px; padding-top:30px;">제작진 목록</h1>
        <div>
            <div class="my-margin-bottom">
                <select v-model="selectedItem" @change="selectItem">
                    <option value="director">감독</option>
                    <option value="actor">배우</option>
                </select>
            </div>
            <ActorListItems v-if="is_actor" :ITEMactors="this.human_list"/>
            <DirectorListItems  v-if="!is_actor" :ITEMdirectors="this.human_list"/>
        </div>
        <infinite-loading ref="infiniteLoading" @infinite="getWholeHumans"></infinite-loading>
    </div>
</template>

<script>
import InfiniteLoading from 'vue-infinite-loading'
import axios from 'axios'
import ActorListItems from '@/components/ActorListItems.vue'
import DirectorListItems from '@/components/DirectorListItems.vue'

export default {
    name:'ActorListView',
    components: {
        ActorListItems,
        DirectorListItems,
        InfiniteLoading
    },
    data() {
        return {
            page:0,
            humans: [],
            selectedItem:"director",
            is_completed:false
        };
    },
    computed:{
        human_list (){
            return this.humans
        },
        is_actor(){
            return (this.selectedItem=='actor')
        }
    },
    methods: {
        selectItem() {
            this.humans = []
            this.page = 0
            this.getWholeHumans()
        },
        getWholeHumans($state){
            if (window.innerHeight + window.pageYOffset < document.body.offsetHeight - 300) {
                return  // 스크롤이 맨 밑에 닿기 전에 300px 이상 위에서는 호출하지 않음
            }
            if (this.selectedItem=='actor'){
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
                        this.humans.push(...res.data)
                        $state.loaded();
                    }else{
                        $state.complete()
                    }
                })
                .catch((err)=>{
                    console.log(err)
                })
            }else{
                axios({
                    method:'get',
                    url:`http://127.0.0.1:8000/api/v1/directors/`,
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
                        this.humans.push(...res.data)
                        $state.loaded();
                    }else{
                        $state.complete()
                    }
                })
                .catch((err)=>{
                    console.log(err)
                })
            }
        }
    },
};

</script>

<style scoped>
.my_MovieListView_BGC {
  background-color: #1C1918;
  border-radius: 5px;
}
.my-margin-bottom{
  margin-bottom: 20px;
}

/* 드롭다운 스타일링 */
select {
  padding: 10px;
  font-size: 16px;
  border: none;
  width: 50%;
  border-radius: 5px;
  background-color: #2C2B2A;
  color: #FFFFFF;
  text-align: center; /* 옵션을 왼쪽에 정렬 */
}

option {
  background-color: #2C2B2A;
  color: #FFFFFF;
  text-align: center; /* 옵션을 왼쪽에 정렬 */
}
</style>