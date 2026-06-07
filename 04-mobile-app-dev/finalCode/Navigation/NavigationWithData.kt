package com.example.navigationcode




import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.navigationcode.ui.theme.NavigationCodeTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            NavigationCodeTheme {
                // Setting up Navigation
                val navController = rememberNavController()  // Initialize NavController

                // NavHost defines the navigation graph for the app
                NavHost(navController = navController, startDestination = "screen1") {
                    composable("screen1") { Screen1(navController) }
                    composable("screen2/{userData}") { backStackEntry ->
                        // Get the passed data from the route arguments
                        val userData = backStackEntry.arguments?.getString("userData") ?: "No Data"
                        Screen2(navController, userData)
                    }
                }
            }
        }
    }
}



@Composable
fun Screen1(navController: NavController) {
    var text by remember { mutableStateOf("") }

    // Box to center the content
    Box(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        contentAlignment = Alignment.Center
    ) {
        Column(horizontalAlignment = Alignment.CenterHorizontally) {
            TextField(
                value = text,
                onValueChange = { text = it },
                label = { Text("Enter your name") },
                modifier = Modifier.fillMaxWidth()
            )
            Spacer(modifier = Modifier.height(16.dp))

            Button(
                onClick = {
                    // Pass data to the next screen through the route
                    navController.navigate("screen2/$text")
                }
            ) {
                Text("Go to Screen 2")
            }
        }
    }
}

@Composable
fun Screen2(navController: NavController, userData: String) {
    // Use Box to center the button
    Box(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        contentAlignment = Alignment.Center
    ) {
        Column(horizontalAlignment = Alignment.CenterHorizontally) {
            Text(text = "Hello, $userData!")

            Spacer(modifier = Modifier.height(16.dp))

            // Simple Back Button
            Button(onClick = {
                // Navigate back to Screen 1
                navController.popBackStack()
            }) {
                Text("Go Back to Screen 1")
            }
        }
    }

}


