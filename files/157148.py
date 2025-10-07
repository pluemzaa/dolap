<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab 1"/>
        <attribute name="authors" value="DELL"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 04:12:59 PM"/>
        <attribute name="created" value="REVMTDtERVNLVE9QLUhKRzBMTU07MjU2OC0wNy0yMDswMjozNTo1OSBQTTsyNjY1"/>
        <attribute name="edited" value="REVMTDtERVNLVE9QLUhKRzBMTU07MjU2OC0wNy0yMDswNDoxMjo1OSBQTTsxOzI3NzA="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="children, adults, total" type="Real" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;-Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;-Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="children"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adults"/>
            <assign variable="total" expression="(children * 120) + (adults * 189)"/>
            <output expression="&quot;You ordered &quot;&amp;children&amp;&quot; children and &quot;&amp;adults&amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp; total &amp;  &quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>