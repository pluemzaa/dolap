<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:23:13 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6NTg6NTMgUE07MjU4NQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MjM6MTMgUE07NDsyNjg1"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="child, adult" type="Integer" array="False" size=""/>
            <declare name="cprice, aprice" type="Integer" array="False" size=""/>
            <declare name="c, a, total" type="Real" array="False" size=""/>
            <assign variable="cprice" expression="120"/>
            <assign variable="aprice" expression="189"/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - &quot;&amp; cprice &amp;&quot; Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - &quot;&amp; aprice &amp;&quot; Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="c"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="a"/>
            <assign variable="total" expression="(c*cprice)+(a*aprice)"/>
            <output expression="&quot;You ordered &quot; &amp; c &amp; &quot;children and &quot;&amp; a &amp; &quot;adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp;total&amp; &quot;Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>