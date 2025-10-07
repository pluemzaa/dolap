<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="TOOD4"/>
        <attribute name="authors" value="KAN"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-20 12:55:43 AM"/>
        <attribute name="created" value="S0FOO0RFU0tUT1AtM1VFTEFFQTsyNTY4LTA3LTE2OzA4OjUwOjUwIFBNOzI1Nzg="/>
        <attribute name="edited" value="S0FOO0RFU0tUT1AtM1VFTEFFQTsyNTY4LTA3LTE2OzA5OjAyOjA0IFBNOzE7MjY4Mw=="/>
        <attribute name="edited" value="c2Fuc287TEFQVE9QLTA3UTVERjFROzIwMjUtMDctMjA7MTI6NTU6NDMgQU07MTsyOTM3"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="fmoney, fyear, lyear, interest" type="Real" array="False" size=""/>
            <assign variable="fyear" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="fmoney"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="lyear"/>
            <while expression="fyear &lt; lyear">
                <assign variable="fyear" expression="fyear + 1"/>
                <assign variable="fmoney" expression="fmoney * (1 + (interest/100))"/>
                <output expression="&quot;Year &quot; &amp; fyear &amp; &quot;: &quot; &amp; fmoney" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>