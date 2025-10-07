<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="AAAA"/>
        <attribute name="authors" value="Sumat"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 04:44:06 PM"/>
        <attribute name="created" value="U3VtYXQ7VE9OR19UT05HX1NIVVI7MjU2OC0wNy0xNjswMzowMjozMyBQTTsyOTQ4"/>
        <attribute name="edited" value="U3VtYXQ7VE9OR19UT05HX1NIVVI7MjU2OC0wNy0xNjswNDo0NDowNiBQTTsyOzMwNjQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="child, adult, total" type="Integer" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children: &quot;" newline="True"/>
            <input variable="child"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="adult"/>
            <assign variable="total" expression="(child*120)+(adult*189)"/>
            <output expression="&quot;You ordered &quot;&amp;child&#13;&#10;&amp;&quot; children and &quot;&#13;&#10;&amp;adult&amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>