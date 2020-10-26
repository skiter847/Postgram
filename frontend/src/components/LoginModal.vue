<template>
  <div class="modal__wrapper">
    <div class="modal">
      <div class="modal__header">
        <span @click="switchLoginModalStatus">X</span>
      </div>
      <div class="modal__title">
        <h2>Postgram</h2>
        <div class="help-text">
          Сервис отложенного постинга в Telegram
        </div>
      </div>

      <div class="modal__content">
        <p>Авторизация с помощью виджета Telegram</p>

        <div class="telegram-auth__wrapper">
          <vue-telegram-login
              mode="callback"
              telegram-login="BotPostram_bot"
              @callback="yourCallbackFunction"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {vueTelegramLogin} from 'vue-telegram-login'
import {mapMutations} from 'vuex'

export default {
  name: "LoginModal",

  components: {
    vueTelegramLogin
  },

  methods: {
    ...mapMutations(['switchLoginModalStatus']),
    yourCallbackFunction(user) {
      // gets user as an input
      // id, first_name, last_name, username,
      // photo_url, auth_date and hash
      console.log(user)
    }
  }
}
</script>

<style scoped>

h2 {
  margin: 0;
  color: black;
  font-weight: bold;
  font-size: 35px;
  text-align: center;
}

.help-text {
  color: gray;
  font-size: 12px;
  text-align: center;
  margin-bottom: 30px;
}

p {
  color: black;
  font-size: 14px;
  text-align: center;
}

.modal__wrapper {
  top: 0;
  left: 0;
  position: fixed;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  display: block;
  transform: translate(-50%, -50%);
  background-color: white;
  width: 500px;
  height: 250px;
}

.telegram-auth__wrapper {
  text-align: center;
}


.modal__header span {
  position: relative;
  font-size: 20px;
  color: black;
  padding: 4px 6px 4px 6px;

}

span:hover {
  background-color: rgba(0, 0, 0, 0.2);
  cursor: pointer;
  border-radius: 8px;
}

.modal__header {
  padding: 10px 10px 10px 0;
  text-align: right;
}

</style>