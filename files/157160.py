<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="TestF1"/>
        <attribute name="authors" value="Legion"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 11:46:05 AM"/>
        <attribute name="created" value="TGVnaW9uO0xBUFRPUC1MN1IwR1VESjsyNTY4LTA3LTE2OzA1OjQ5OjIzIFBNOzI5NzY="/>
        <attribute name="edited" value="TGVnaW9uO0xBUFRPUC1MN1IwR1VESjsyNTY4LTA3LTIxOzExOjQ2OjA1IEFNOzM7MzA2MQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Child, Adult, total" type="Integer" array="False" size=""/>
            <output expression="&quot;price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="Child"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="Adult"/>
            <assign variable="total" expression="(Adult*189)+(Child*120)"/>
            <output expression="&quot;You ordered &quot; &amp; (Child) &amp; &quot; children &quot; &amp; &quot; and &quot;&amp;(Adult)&amp;&quot; adults &quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp; (total)&amp;&quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>