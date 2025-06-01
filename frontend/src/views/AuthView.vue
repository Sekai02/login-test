<template>
  <v-container fluid class="d-flex align-center justify-center fill-height">
    <v-card width="400" elevation="10">
      <div class="d-flex justify-center">
        <v-img
          src="@/../images/stellantis-and-you-logo-blue.png"
          contain
          max-height="200"
          max-width="200"
          class="mb-4"
        />
      </div>

      <v-card-title class="text-h5 text-center">
        {{ isLogin ? 'Bienvenido' : 'Registro' }}
      </v-card-title>

      <v-card-text>
        <v-form>
          <v-text-field v-if="!isLogin" v-model="name" label="Nombre" required />

          <v-text-field v-model="email" label="Email" type="email" required />
          <v-text-field
            v-model="password"
            :type="showPassword ? 'text' : 'password'"
            label="Contraseña"
            required
            append-inner-icon="mdi-eye"
            @click:append-inner="togglePasswordVisibility"
          />

          <!-- Optional extra field for register -->
          <v-text-field
            v-if="!isLogin"
            v-model="confirmPassword"
            :type="showConfirmPassword ? 'text' : 'password'"
            label="Confirmar Contraseña"
            required
            append-inner-icon="mdi-eye"
            @click:append-inner="toggleConfirmPasswordVisibility"
          />

          <v-btn class="mt-4 navy-button" block @click="handleSubmit">
            {{ isLogin ? 'Iniciar Sesión' : 'Registrarse' }}
          </v-btn>
        </v-form>
      </v-card-text>

      <v-card-actions class="justify-center">
        <v-btn variant="text" @click="isLogin = !isLogin">
          {{
            isLogin ? '¿No tienes una cuenta? Regístrate' : '¿Ya tienes una cuenta? Iniciar sesión'
          }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const isLogin = ref(true)
const name = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const showPassword = ref(false)
const showConfirmPassword = ref(false)

function togglePasswordVisibility() {
  showPassword.value = !showPassword.value
}

function toggleConfirmPasswordVisibility() {
  showConfirmPassword.value = !showConfirmPassword.value
}

function handleSubmit() {
  if (isLogin.value) {
    console.log('Login with', email.value, password.value)
    // TODO: Send login request
  } else {
    console.log('Register with', email.value, password.value, confirmPassword.value)
    // TODO: Validate and send register request
  }
}
</script>

<style scoped>
.navy-button {
  background-color: #243782;
  color: white;
}
</style>