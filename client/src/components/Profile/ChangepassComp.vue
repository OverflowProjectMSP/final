<script>
import axios from 'axios';
export default {
    data() {
        return {
            oldPassword: ``,
            newPassword: ``,
            exPassword: ``,
            error: '',
            id:'',
            isInSession: false,
        }
    },

    methods: {
        check(){
            if (!this.newPassword.includes('~') && 
                !this.newPassword.includes('`') && 
                !this.newPassword.includes('!') && 
                !this.newPassword.includes('@') && 
                !this.newPassword.includes('#') && 
                !this.newPassword.includes('%') && 
                !this.newPassword.includes('^') && 
                !this.newPassword.includes('&') && 
                !this.newPassword.includes('*') && 
                !this.newPassword.includes('(') && 
                !this.newPassword.includes(')') && 
                !this.newPassword.includes('-') && 
                !this.newPassword.includes('_') && 
                !this.newPassword.includes('=') && 
                !this.newPassword.includes('+') && 
                !this.newPassword.includes('[') && 
                !this.newPassword.includes(']') && 
                !this.newPassword.includes('{') && 
                !this.newPassword.includes('}') && 
                !this.newPassword.includes('\\') && 
                !this.newPassword.includes('|') && 
                !this.newPassword.includes(';') && 
                !this.newPassword.includes(':') && 
                !this.newPassword.includes('"') && 
                !this.newPassword.includes(',') && 
                !this.newPassword.includes('<') && 
                !this.newPassword.includes('.') && 
                !this.newPassword.includes('>') && 
                !this.newPassword.includes('/') && 
                !this.newPassword.includes('?')) {
                    this.error = '*Пароль должен включать спец символ*';
                } else if (this.newPassword.includes('$')) {
                    this.error = '*Ты че, не патриот? Доллары всякие тут ставишь*';
                } else {
                    this.putInfo();
                }
        },
        async putInfo() {
            if (this.newPassword == this.exPassword ) {
                let res = await axios.put('/new-password-old', {
                    old_password: this.oldPassword,
                    new_password: this.newPassword,
                });
                if (res.data.res == 'Error') {
                    this.error = '*Ошибка отправки*';
                } else if (res.data.res == 'True') {
                    this.$router.push(`/Profile?id=${this.id}`);
                } else {
                    this.error = 'Неизветсная ошибка';
                }
            } else {
                this.error = 'Пароли не совпадают';
            }


        },
        async getId(){
            let res = await axios.get(`/session`);
            this.id = res.data.id;
            if(!this.id) {
                this.$router.push('/Login')
            }
        }
    },
    mounted(){
        this.getId()
    }
}
</script><template>
<form @submit.prevent="check" v-if="this.id"> 
  <div class="window">
    <div class="change-block">
      <h1>Изменить пароль</h1>
      <div class="ancet d-flex" style="display: flex; gap: 40px;">
          <h5 role="button" class="mb-0" style="color: gray; font-weight: 400;"><a href="/NewSetting">Анкета</a>
          </h5>
          <h5 role="button" class="mb-0 border-bottom border-2 border-dark"><a href="/Changepass">Аккаунт</a>
          </h5>
      </div>

      <div class="inputs">
        <div class="old-pass">
          <input type="password" v-model="oldPassword">
          <span>Старый пароль</span>  
        </div>
        <div class="new-pass">
          <input type="password" v-model="newPassword">
          <span>Новый пароль</span>
        </div>
        <div class="res-pass">
          <input type="password" v-model="exPassword">
          <span>Повторите пароль</span>
        </div>
        <div class="save">
          <button type="submit">Сохранить изменениия</button>
        </div>

      </div>
    </div>
  </div>
</form>
</template>

<style scoped>

.ancet {
  margin-bottom: 60px;
}

.save {
  display: flex;
  justify-content: start;
  width: 100%;
}

.save button {
    background-color: rgb(255, 255, 255);
    font-size: 20px;
    font-weight: 500;
    color: #7ac97a;
    border: 2px solid #7ac97a;
    border-radius: 8px;
    width: 360px;
    text-align: center;
    transition: all 200ms;
    width: 300px;
    height: 40px;
}

.save button:hover {
  background-color: #7ac97a;
  color: #ffffff;
}

.save button:active {
  background-color: #5ba35b;
}

.window {
  width: 100%;
  height: 600px;

  display: flex;
  justify-content: center;
}

.change-block {
  width: 60%;
}

.inputs {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
}

.inputs div {
  width: 70%;
}

input {
  width: 100% !important;

  width: 300px;
  height: 40px;
  border: 2px solid #000;
  background-color: #fff;
  border-radius: 8px;
  font-size: 20px;
  padding: 0 10px;
}

.change-block h1 {
  border-bottom: 2px solid #000;
  padding-bottom: 20px;
  font-size: 30px;
}

.old-pass input {
 
}

.old-pass {
  position: relative;
}

.old-pass span {
  position: absolute;
  left: 10px;
  top: -22px;
  background-color: #3b82f6;
  padding: 1px 20px;
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  border-radius: 8px;
}

.new-pass input {
  
}

.new-pass {
  position: relative;
}

.new-pass span {
  position: absolute;
  left: 10px;
  top: -22px;
  background-color: #3b82f6;
  padding: 1px 20px;
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  border-radius: 8px;
}


.res-pass input {
}

.res-pass {
  position: relative;
}

.res-pass span {
  position: absolute;
  left: 10px;
  top: -22px;
  background-color: #3b82f6;
  padding: 1px 20px;
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  border-radius: 8px;
}

@media (max-width: 830px) {
  .change-block {
    width: 80%;
  }
}

@media (max-width: 530px) {
  .inputs div {
    width: 100%;
  }
}


















</style>
