package com.example.sharedpeferences

import android.content.Context
import android.content.Intent
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import com.example.sharedpeferences.ui.theme.SharedPeferencesTheme
import androidx.core.content.edit

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        setContent {
            SharedPeferencesTheme {

                var showGreeting by remember { mutableStateOf(false) }

                if (showGreeting) {
                    Greeting()
                } else {
                    MainScreen(
                        onSaveClick = {
                            showGreeting = true
                        }
                    )
                }
            }
        }
    }
}

@Composable
fun MainScreen(onSaveClick: () -> Unit) {

    val context = LocalContext.current
    val sharedPreferences = context.getSharedPreferences("MyPrefs", Context.MODE_PRIVATE)

    var name by remember { mutableStateOf("Hanseeka") }
    var email by remember { mutableStateOf("abc@gmail.com") }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.Center
    ) {

        OutlinedTextField(
            value = name,
            onValueChange = { name = it },
            label = { Text("Name") },
            modifier = Modifier.fillMaxWidth()
        )

        Spacer(modifier = Modifier.height(8.dp))

        OutlinedTextField(
            value = email,
            onValueChange = { email = it },
            label = { Text("Email") },
            modifier = Modifier.fillMaxWidth()
        )

        Spacer(modifier = Modifier.height(16.dp))

        Button(
            onClick = {
                // Save data to SharedPreferences
                sharedPreferences.edit {
                    putString("name", name)
                        .putString("email", email)
                }

                // Move to GreetingActivity
                onSaveClick()
            },
            modifier = Modifier.fillMaxWidth()
        ) {
            Text("Save")
        }
    }
}
