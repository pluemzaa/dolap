<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="work1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:20:14 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzowMzo1NyBQTTsyNTQ3"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzoyMDoxNCBQTTsxOzI2NDc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="child, adult, total" type="Real" array="False" size=""/>
            <declare name="num1, num2" type="Integer" array="False" size=""/>
            <assign variable="num1" expression="0"/>
            <assign variable="num2" expression="0"/>
            <assign variable="child" expression="120"/>
            <assign variable="adult" expression="189"/>
            <assign variable="total" expression="0"/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person &quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="num1"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="num2"/>
            <assign variable="total" expression="(num1 * 120) + (num2 * 189)"/>
            <output expression="&quot;You ordered &quot; &amp; num1 &amp;&quot; children and &quot;&amp; num2 &amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp; total &amp;&quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>