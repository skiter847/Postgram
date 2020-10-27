<template>
  <div class="add-channel">
    <span> + Добавить канал</span>
  </div>
</template>

<script>
export default {
  name: "ChannelsList"
}
</script>

<style scoped>

.add-channel {
  padding-top: 10px;
  display: flex;
  flex: 0 0 25%;
  justify-content: center;
}

.add-channel span {
  font-size: 15px;
  padding: 10px 25px 10px 25px;
  color: white;
  font-weight: bold;
  background-color: #5580a3;
  cursor: pointer;
}

.add-channel span:hover{
  background-color: #497799;
}

</style>