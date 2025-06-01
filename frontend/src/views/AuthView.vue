<template>
  <v-container fluid class="d-flex align-center justify-center fill-height">
    <v-card width="400" elevation="10">
      <v-card-title class="text-h5 text-center">
        {{ isLogin ? 'Login' : 'Register' }}
      </v-card-title>

      <v-card-text>
        <v-form>
          <v-text-field
            v-model="email"
            label="Email"
            type="email"
            required
          />
          <v-text-field
            v-model="password"
            label="Password"
            type="password"
            required
          />

          <!-- Optional extra field for register -->
          <v-text-field
            v-if="!isLogin"
            v-model="confirmPassword"
            label="Confirm Password"
            type="password"
            required
          />

          <v-btn
            class="mt-4"
            color="primary"
            block
            @click="handleSubmit"
          >
            {{ isLogin ? 'Login' : 'Register' }}
          </v-btn>
        </v-form>
      </v-card-text>

      <v-card-actions class="justify-center">
        <v-btn variant="text" @click="isLogin = !isLogin">
          {{ isLogin ? "Don't have an account? Register" : "Already have an account? Login" }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const isLogin = ref(true)
const email = ref('')
const password = ref('')
const confirmPassword = ref('')

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
