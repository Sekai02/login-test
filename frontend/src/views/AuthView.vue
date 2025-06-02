<template>
  <v-container fluid class="d-flex align-center justify-center fill-height">
    <v-card width="400" elevation="10">
      <div class="d-flex justify-center">
        <v-img
          src="/images/stellantis-and-you-logo-blue.png"
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
        <v-form @submit.prevent="handleSubmit" ref="formRef">
          <v-text-field
            v-if="!isLogin"
            v-model="name"
            :rules="[(v) => !!v || 'Nombre requerido']"
            label="Nombre"
            required
          />

          <v-text-field v-model="email" label="Email" type="email" :rules="emailRules" required />

          <v-text-field
            v-model="password"
            :type="showPassword ? 'text' : 'password'"
            :rules="[(v) => !!v || 'Contraseña requerida']"
            label="Contraseña"
            required
            append-inner-icon="mdi-eye"
            @click:append-inner="togglePasswordVisibility"
          />

          <!-- Password strength meter -->
          <v-progress-linear
            v-if="!isLogin && password"
            :model-value="passwordStrength"
            :color="passwordStrengthColor"
            height="6"
            class="mb-2"
          />
          <div v-if="!isLogin && password" class="text-caption mb-2">
            Seguridad: {{ passwordStrengthLabel }}
          </div>

          <v-text-field
            v-if="!isLogin"
            v-model="confirmPassword"
            :type="showConfirmPassword ? 'text' : 'password'"
            :rules="[(v) => v === password || 'Las contraseñas no coinciden']"
            label="Confirmar Contraseña"
            required
            append-inner-icon="mdi-eye"
            @click:append-inner="toggleConfirmPasswordVisibility"
          />

          <v-checkbox
            v-if="!isLogin"
            v-model="termsAccepted"
            :rules="termsRules"
            required
            class="mt-2"
            hide-details="auto"
          >
            <template #label>
              Acepto los
              <a href="#" target="_blank" class="terms-link"> Términos y Condiciones</a>
            </template>
          </v-checkbox>

          <v-btn
            class="mt-4 navy-button"
            block
            type="submit"
            :loading="loading"
            :disabled="loading"
          >
            {{ isLogin ? 'Iniciar Sesión' : 'Registrarse' }}
          </v-btn>
        </v-form>
      </v-card-text>

      <v-card-actions class="justify-center">
        <v-btn variant="text" @click="switchMode" :disabled="loading">
          {{
            isLogin ? '¿No tienes una cuenta? Regístrate' : '¿Ya tienes una cuenta? Iniciar sesión'
          }}
        </v-btn>
      </v-card-actions>
    </v-card>

    <!-- Snackbar -->
    <v-snackbar v-model="snackbar.show" :color="snackbar.color" :timeout="3000">
      {{ snackbar.message }}
    </v-snackbar>
  </v-container>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

const isLogin = ref(true)
const name = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const showPassword = ref(false)
const showConfirmPassword = ref(false)
const formRef = ref()
const loading = ref(false)
const termsAccepted = ref(false)

const snackbar = ref({
  show: false,
  message: '',
  color: 'success',
})

function showSnackbar(message: string, color = 'success') {
  snackbar.value.message = message
  snackbar.value.color = color
  snackbar.value.show = true
}

const emailRules = [
  (v: string) => !!v || 'Email requerido',
  (v: string) => /.+@.+\..+/.test(v) || 'Email inválido',
]

const termsRules = [(v: boolean) => v || 'Debes aceptar los Términos y Condiciones']

function togglePasswordVisibility() {
  showPassword.value = !showPassword.value
}

function toggleConfirmPasswordVisibility() {
  showConfirmPassword.value = !showConfirmPassword.value
}

function calculatePasswordStrength(pw: string): number {
  let strength = 0
  if (pw.length >= 6) strength += 20
  if (pw.length >= 10) strength += 20
  if (/[a-z]/.test(pw)) strength += 20
  if (/[A-Z]/.test(pw)) strength += 20
  if (/\d/.test(pw)) strength += 10
  if (/[^A-Za-z0-9]/.test(pw)) strength += 10
  return strength
}

const passwordStrength = computed(() => calculatePasswordStrength(password.value))
const passwordStrengthLabel = computed(() => {
  const s = passwordStrength.value
  if (s <= 30) return 'Débil'
  if (s <= 60) return 'Media'
  return 'Fuerte'
})
const passwordStrengthColor = computed(() => {
  const s = passwordStrength.value
  if (s <= 30) return 'red'
  if (s <= 60) return 'orange'
  return 'green'
})

function resetForm() {
  name.value = ''
  email.value = ''
  password.value = ''
  confirmPassword.value = ''
  termsAccepted.value = false
  formRef.value?.reset()
}

function switchMode() {
  isLogin.value = !isLogin.value
  resetForm()
}

async function handleSubmit() {
  const form = formRef.value
  const valid = await form?.validate()

  if (!valid.valid) return

  loading.value = true

  try {
    if (isLogin.value) {
      // Simulate login API
      console.log('Login with', email.value, password.value)
      showSnackbar('Inicio de sesión exitoso')
    } else {
      // Simulate registration API
      console.log('Register with', name.value, email.value, password.value)
      showSnackbar('Registro exitoso')
    }
  } catch (err) {
    showSnackbar('Ocurrió un error', 'error')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.navy-button {
  background-color: #243782;
  color: white;
}
.terms-link {
  color: #243782;
  text-decoration: underline;
  margin-left: 4px;
}
</style>
