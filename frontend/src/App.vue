<template>
  <div class="container">
    <header class="row">
      <div class="header__menu">
        <a class="nav-btn">
          <div class="nav-item"></div>
          <div class="nav-item"></div>
          <div class="nav-item"></div>
        </a>
        <span>Postgram</span>
      </div>
    </header>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {}
}
</script>


<style>
body {
  font: 13px/18px Tahoma,sans-serif,Arial,Helvetica;
  background-color: #e7ebf0;
}

span{
  font-size: 21px;
  padding-left: 25%;
}

.header__menu {
  display: flex;
  flex: 0 0 25%;
  padding: 17px;
  align-items: center;
}

.header__menu:hover{
  background-color: #497799;
}

.nav-btn:hover{
  cursor: pointer;
}

.nav-item{
    width: 18px;
    height: 2px;
    background-color: white;
    margin: 4px 0;
}

header {
  background-color: #5580a3;
  color: white;
}
</style>
