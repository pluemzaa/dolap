<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="LAP1fi"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 06:33:02 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6NTc6MTggUE07MjU4Nw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6MzM6MDIgUE07MzsyNjg1"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="monny, child, adult, Totel" type="Integer" array="False" size=""/>
            <assign variable="child" expression="0"/>
            <assign variable="adult" expression="0"/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="child"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adult"/>
            <declare name="chi, adu, toppp" type="Integer" array="False" size=""/>
            <assign variable="chi" expression="child * 120"/>
            <assign variable="adu" expression="adult * 189"/>
            <assign variable="toppp" expression="adu + chi"/>
            <output expression="&quot;You ordered &quot;&amp; child &amp;&quot; children and &quot;&amp; adult &amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp; toppp &amp;&quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>