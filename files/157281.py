<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="work1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 03:20:58 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzowMzo1OCBQTTsyNTQ4"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMzoyMDo1OCBQTTs2OzI2NjA="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="children, adults, total, adultPrice, childPrice" type="Real" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <assign variable="childPrice" expression="120"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <assign variable="adultPrice" expression="189"/>
            <output expression="&quot;Enter number of children: &quot;" newline="True"/>
            <input variable="children"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="adults"/>
            <assign variable="total" expression="(children * childPrice) + (adults * adultPrice)"/>
            <output expression="&quot;You ordered &quot;&amp;children&amp;&quot; children and &quot;&amp;adults&amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp;total&amp;&quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>