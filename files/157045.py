<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="REAL1.1"/>
        <attribute name="authors" value="sanso"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:58:55 PM"/>
        <attribute name="created" value="c2Fuc287TEFQVE9QLTA3UTVERjFROzIwMjUtMDctMTY7MDM6NTM6NTIgUE07Mjg0Nw=="/>
        <attribute name="edited" value="c2Fuc287TEFQVE9QLTA3UTVERjFROzIwMjUtMDctMTY7MDQ6NTg6NTUgUE07MTU7MzAxNw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="child" type="Integer" array="False" size=""/>
            <declare name="adult" type="Integer" array="False" size=""/>
            <declare name="total" type="Integer" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="child"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adult"/>
            <assign variable="total" expression="(child * 120) + (adult * 189)"/>
            <output expression="&quot;You ordered &quot;&amp; child &amp;&quot; children and &quot; &amp; adult &amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>