<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_4"/>
        <attribute name="authors" value="Lenovo"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 12:17:50 PM"/>
        <attribute name="created" value="TGVub3ZvO0xBUFRPUC1GMk9BVDRQSTsyNTY4LTA3LTIwOzExOjQ3OjUyIEFNOzI5Njg="/>
        <attribute name="edited" value="TGVub3ZvO0xBUFRPUC1GMk9BVDRQSTsyNTY4LTA3LTIwOzEyOjE3OjUwIFBNOzE7MzA4Nw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interesrate" type="Real" array="False" size=""/>
            <declare name="years, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interesrate"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="years"/>
            <for variable="i" start="1" end="years" direction="inc" step="1">
                <assign variable="money" expression="money * (1+interesrate / 100)"/>
                <output expression="&quot;Year &quot; &amp; i &amp; &quot;: &quot; &amp; money" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>