3. Tutorial: How to add new sections in the future
When you want to add a new section (e.g., "thermo.html" for Thermodynamics), follow these 3 simple steps:

Step 1: Create the file
Create a new file in your sections folder (e.g., sections/thermo.html) and paste your cards in there.

Step 2: Add the Sidebar Link
Open index.html. Scroll to the <nav> section and add a link with a new data-filter name.

HTML

<a href="#" class="nav-link js-filter" data-filter="thermo">Thermodynamics</a>
Step 3: Register the file in JavaScript
Scroll to the bottom of index.html to the <script> tag. Look for the contentFiles list and add your new file path.

JavaScript

const contentFiles = [
  './sections/calculus.html',
  './sections/multivar.html',
  './sections/waves.html',
  './sections/thermo.html' // <--- Add this comma and line
];
That's it! The system will automatically fetch the file, load the cards, and the filter button will work immediately.