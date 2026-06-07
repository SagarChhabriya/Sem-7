package com.example.navigationcode


import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.navigationcode.ui.theme.NavigationCodeTheme

class SimpleNavigation : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            NavigationCodeTheme {
                // Setting up Navigation
                val navController = rememberNavController()  // Initialize NavController

                // NavHost defines the navigation graph for the app
                NavHost(navController = navController, startDestination = "screen1") {
                    composable("screen1") { FirstScreen1(navController) }
                    composable("screen2") { SecondScreen2(navController) }
                }
            }
        }
    }
}


@Composable
fun FirstScreen1(navController: NavController) {
    // Use Box to center the button
    Box(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        contentAlignment = Alignment.Center
    ) {
        Button(onClick = {
            // Navigate to screen2 when the button is clicked
            navController.navigate("screen2")
        }) {
            Text("Go to Screen 2")
        }
    }
}

@Composable
fun SecondScreen2(navController: NavController) {
    // Use Box to center the button
    Box(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        contentAlignment = Alignment.Center
    ) {
        Button(onClick = {
            // Navigate back to screen1
            navController.popBackStack()
        }) {
            Text("Go Back to Screen 1")
        }
    }
}
