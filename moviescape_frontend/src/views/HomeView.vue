<template>
  <div>
    <div class="section black">
      <h1 class="my-bold-story">
        Short Movie storys
        <br>
        to feel, do, live
        <br>
      </h1>
      <div class="my-dis">
        <div></div>
        <img style="width: 500px;" src="@/assets/MainLogo.png" alt="">
        <h2>MOVIESCAPE
          <br>
      <div class="my-line">
      </div>
          <br>
          <br>
        </h2>
      </div>
      <br>

    </div>
    <div class="section black">
      <div>
        <h1 class="my-bold">
          짧은 이야기, 그 이상의 경험과 공감을 위해
          <br> 
          MOVIESCAPE는 단순한 시각적 경험에서 벗어나,
          <br>
          더 나은 경험을 사용자에게 제공하기 위한 커뮤니티 입니다.
          <hr>
        </h1>
      </div>
    </div>
    <div class="section black">
      <h1 class="my-bold-story" style="margin-right:200px;">
        MAIN KEY COLOR인
        <br>
        #008080은 넓고 푸른
        <br>
        feel을 의미하고
        <br>
      </h1>
      <div class="my-box my-dis"></div>
    </div>
    <div class="section black">
      <div class="my-box2 my-dis"></div>
      <h1 class="my-bold-story" style="margin-left:200px;">
        SUB KEY COLOR인
        <br>
        rgb(255, 90, 0)은 
        <br>
        열정의 빛을 띄는
        <br>
        do를 의미합니다.
        <br>
      </h1>
    </div>
    <div class="section black">
      <h1 class="my-bold-story my-box3 my-dis" style="margin-left:200px;">
        그리고 배경의 COLOR #000000는 
        <br>
        MAIN COLOR와 SUB COLOR가 만나
        <br>
        만들어지는 우리의 이야기
        <br>
        live를 의미합니다.
        <br>
      </h1>
    </div>

    <!-- <div class="section black">
      <div>
        <h1 class="my-bold">
          MAIN KEY COLOR인 #008080은 
          <br> 
          MOVIESCAPE는 시각적 경험에 그치지 않고,
          <br>
          더 나은 경험을 사용자에게 제공하기 위한 커뮤니티 입니다.
          <hr>
        </h1>
      </div>
    </div> -->
    <!-- <div class="section teal">
      <div>
      </div>
    </div> -->
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style>
.my-box2{
  border: 1px rgb(255, 90, 0);
  background-color: rgb(255, 90, 0);
  width:500px;
  height:700px;
}
.my-box{
  border: 1px #008080;
  background-color: #008080;
  width:500px;
  height:700px;
}
.my-line{
  border: solid 4px white;
  width:100%;
  margin-right:auto;
}
.my-bold-story{
  font-weight: bold;
  font-size: 60px;
}

.my-bold {
  font-weight: bold;
  font-size: 50px; /* 원하는 크기로 조정해주세요 */
}

.my-dis {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  animation: moveUpDown 2s infinite alternate;
}

@keyframes moveUpDown {
  0% {
    transform: translateY(-5px);
  }
  100% {
    transform: translateY(5px);
  }
}

.section {
  width: 100vh;
  height: 1000px;
  background-color: black;
  display: flex;
  align-items: center;
  justify-content: center;
}

.black {
  background-color: #000000;
}

.gray {
  background-color: #808080;
}

.teal {
  background-color: #008080;
}
</style>
