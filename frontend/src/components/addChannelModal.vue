<template>
  <div class="modal__wrapper">
    <div class="modal" v-bind:style="{width : modalWidth, height : modalHeight}">
      <div class="modal__inner">
        <h3>Добавление канала</h3>
        <p>Добавьте бота <span>@BotPostram_bot</span> в список администраторов канала с правами на управление постами.
        </p>
        <div class="check_correct">
          <p>Чтобы убедиться в том что вы сделали все правильно, введите ссылку на ваш канал в поле.</p>
          <div class="input__wrapper">
            <input type="text" placeholder="https://t.me/SomeChannel" v-model="inputText">
          </div>
        </div>
        <div class="button__wrapper">
          <button @click="switchAddChannelStatus">назад</button>
          <button type="submit" v-bind:class="{ disabled: getInputStatus }">Проверить</button>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import {mapMutations} from 'vuex';


export default {
  name: "AddChannelModal",
  data() {
    return {
      inputText: "",
      inputClear: true,
      modalWidth: '500px',
      modalHeight: '350px',
    }
  },

  computed: {
    getInputStatus() {
      return this.inputClear
    },
  },

  watch: {
    inputText: function () {
      if (this.inputText !== "") {
        this.inputClear = false
      } else {
        this.inputClear = true
      }
    }
  },

  methods: {
    ...mapMutations(['switchAddChannelStatus']),
  },
}
</script>

<style scoped>

h3 {
  text-align: center;
  font-weight: bold;
  margin-bottom: 40px;
}

p {
  font-size: 16px;
  padding: 0 10px 0 10px;
}

span {
  color: blue;
  font-weight: bold;
}

.button__wrapper {
  display: flex;
  justify-content: flex-end;
  margin-top: 45px;
}

.input__wrapper {
}

button:first-child {
  margin-right: 15px;
}

button {
  text-transform: uppercase;
  padding: 10px;
  border-radius: 8px;
  background-color: #5580a3;
  border: none;
  outline: none;
  color: white;
  font-size: 18px;
}

.disabled {
  background-color: rgba(0, 0, 0, 0.2);
  color: rgba(0, 0, 0, 0.5);
  cursor: default;
}

input {
  font-size: 18px;
  width: 100%;
  outline: none;
  border: none;
  border-bottom: 1px solid rgba(0, 0, 0, 0.5);
}

.modal__wrapper {
  top: 0;
  left: 0;
  position: fixed;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.2);
}

.modal__inner {
  height: 100%;
  padding: 25px;
}

.modal {
  display: flex;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
}

</style>