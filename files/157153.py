<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="anslab_1"/>
        <attribute name="authors" value="ateru"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 06:33:33 PM"/>
        <attribute name="created" value="YXRlcnU7VEhBTlBJVENIQTsyMDI1LTA3LTE2OzA1OjQ5OjExIFBNOzI1NzI="/>
        <attribute name="edited" value="YXRlcnU7VEhBTlBJVENIQTsyMDI1LTA3LTE2OzA2OjMzOjMzIFBNOzQ7MjY4MQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="priceAdult, priceChild" type="Integer" array="False" size=""/>
            <declare name="num1, num2, result" type="Real" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="num1"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="num2"/>
            <assign variable="result" expression="(num1*120)+(num2*189)"/>
            <output expression="&quot;You ordered &quot;&amp;num1&amp;&quot; children and &quot;&amp;num2&amp;&quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp;result&amp;&quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>