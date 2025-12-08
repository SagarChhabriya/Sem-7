# **ANDROID BASICS**

### **1. Introduction to Android**

A mobile operating system by Google used to build apps for smartphones and tablets.
**Example:** WhatsApp is an Android application.

### **2. Installation of Android Studio**

Android Studio is the official IDE for Android app development.
**Example:** Install Android Studio → create a new project → run on emulator.

### **3. Android Architecture & Runtime Environment**

Layers include Applications, Framework, Libraries, and Linux Kernel. Runs apps using ART (Android Runtime).
**Example:** When you open an app, ART compiles and runs it.

### **4. First Android App (Hello World!)**

Your first project that prints “Hello World!” on the screen.
**Example:** Default template shows a TextView saying *Hello World*.



# **ANDROID XML LAYOUTS**

### **1. Constraint Layout**

Layout where you place views by constraining them to each other or parent.
**Example:** Button centered by tying all four sides to parent.

### **2. Relative Layout**

Views positioned relative to others.
**Example:** Button below a TextView.

### **3. Linear Layout**

Arranges views in a vertical or horizontal line.
**Example:** Column of TextView → EditText → Button.

### **4. GridView**

Shows items in a grid format.
**Example:** Gallery app showing images in rows & columns.

### **5. Table Layout**

Arranges views in rows and columns.
**Example:** Calculator UI.

### **6. Weight & Gravity**

* **Weight:** how screen space is shared
* **Gravity:** alignment inside a view
  **Example:** Two buttons 50/50 width using `layout_weight`.



# **ANDROID WIDGETS**

### **1. TextView**

Displays text.
**Example:** `<TextView android:text="Hello"/>`

### **2. EditText**

Input field to type text.
**Example:** Enter username.

### **3. Button**

Clickable component.
**Example:** Login button.



# **JETPACK COMPOSE BASICS**

### **1. What is Jetpack Compose?**

Modern UI toolkit for building Android UI using Kotlin code.
**Example:** `Text("Hello Compose")`.

### **2. Why use Jetpack Compose?**

Less boilerplate, faster UI development.
**Example:** No XML needed.

### **3. Comparison with XML**

Compose uses Kotlin functions; XML is static layout files.
**Example:** Compose uses `Column {}` instead of `<LinearLayout>`.



# **GETTING STARTED WITH COMPOSE**

### **Composable Functions**

Functions that describe UI.
**Example:**

```kotlin
@Composable
fun Greeting() { Text("Hi") }
```

### **Anatomy**

Annotation + parameters + UI code.
**Example:** `@Composable fun MyUI(name: String)`



# **COMPOSE UI COMPONENTS**

### **Text / Button / Image / TextField**

UI elements written in Kotlin.
**Example:** `Button(onClick={}){ Text("Click") }`

### **Checkbox/Radio/Switch**

Selectable UI controls.
**Example:** `Checkbox(checked = true, onCheckedChange={})`

### **Modifiers**

Used to style or position elements.
**Example:** `Modifier.padding(16.dp)`



# **COMPOSE LAYOUTS**

### **Column, Row, Box**

Layout containers.
**Example:** Column for vertical list.

### **Nesting Layouts**

Putting layouts inside others.
**Example:** Column → Row → Text.

### **Modifiers for Layout**

Controls size, alignment, padding.
**Example:** `Modifier.fillMaxWidth()`



# **STATE IN COMPOSE**

### **State**

Stores UI values that change.
**Example:** Click counter.

### **Mutable State**

Variable that updates UI automatically.
Example:

```kotlin
var count by remember { mutableStateOf(0) }
```

### **State Hoisting**

Move state to a parent for reusability.
**Example:** Parent controls a child's TextField value.

### **ViewModel + LiveData**

Stores data independent of screen rotation.
**Example:** ViewModel holds user input.



# **INTENTS**

### **1. Explicit Intent**

Open another activity in same app.
**Example:** Open ProfileActivity.

### **2. Implicit Intent**

Ask system to perform an action.
**Example:** Open camera → `ACTION_IMAGE_CAPTURE`

### **3. Intent Filters**

Declare which actions your app can handle.
**Example:** Handle shared images.



# **NAVIGATION (COMPOSE)**

### **Navigation Basics**

Moving between screens.
**Example:** Navigate from Home to Details.

### **Passing Data**

Send values to next screen.
**Example:** `navController.navigate("detail/5")`

### **Deep Links**

Open a screen from a URL.



# **PREFERENCES**

### **1. App State Preferences**

Store simple data permanently.
**Example:** Save login status.

### **2. Activity Shared Preferences**

Store activity-level small data.
**Example:** Store username.



# **FILE STORAGE**

### **Reading/Writing Files**

Store text in internal storage.
**Example:** Write notes to a file.

### **Raw & Online Files**

Read files placed in *res/raw* or from internet.

### **Lists & Widgets**

Show items using ListView/RecyclerView.

### **SQLite**

Built-in database for apps.
**Example:** Save student records.



# **USER INPUT & COROUTINES**

### **Handling User Input**

Process clicks, typing, gestures.
**Example:** Button click.

### **Coroutines**

Lightweight threads for background work.
**Example:** Fetch API using `CoroutineScope`.



# **SERVICES & THREADS**

### **Services**

Background tasks.
**Example:** Music player.

### **Foreground Service**

Runs with a notification.
**Example:** Location tracking.

### **Threads**

Separate line of execution.
**Example:** Run heavy computation.



# **NOTIFICATIONS**

### **Notifications**

Alert shown in status bar.
**Example:** New message notification.



# **WORKMANAGER**

### **Worker Class**

Defines background work.
**Example:** Upload logs.

### **OneTimeRequest / PeriodicRequest**

Run once or repeatedly.
**Example:** Sync every 15 minutes.

### **Constraints**

Conditions like Wi-Fi only.

### **Getting Results**

Worker returns success or failure.



# **CONTENT PROVIDERS**

### **Reading Content Providers**

Access shared data like contacts.
**Example:** Read contacts list.

### **Creating Provider**

Expose your app’s data to others.



# **NETWORKING**

### **OkHTTP**

Library for HTTP requests.
**Example:** GET request to API.

### **Sending/Receiving Response**

Convert JSON to objects.

### **JSON/XML Parsing**

Process API data.



# **FLUTTER & DART**

### **Flutter**

UI toolkit by Google to build Android, iOS, Web apps.
**Example:** Single codebase for all platforms.

### **Dart**

Programming language used by Flutter.
**Example:** `print("Hello")`.

### **Hello World Flutter**

Basic Flutter app showing text.



# **FLUTTER WIDGETS**

### **Scaffold**

Basic page layout.
**Example:** AppBar + Body.

### **Image / Container / Icon**

Basic UI building blocks.

### **Column/Row**

Arrange widgets.

### **Card**

Material design card.

### **Buttons**

Interactive widgets
**Example:** FloatingActionButton.

### **Inputs**

Checkbox, Radio, Slider.



# **FLUTTER LAYOUTS**

Arranging widgets using Column/Row/Stack.
**Example:** Stack to overlap widgets.



# **DIALOGS**

Popup windows.
**Example:** AlertDialog.



# **ROUTERS**

Navigation between screens.
**Example:** `Navigator.push()`.



# **STATE MANAGEMENT**

Managing UI changes.
**Example:** `setState()` to update counter.


