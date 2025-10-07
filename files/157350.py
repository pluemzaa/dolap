<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="LabT4_4"/>
        <attribute name="authors" value="Kkulib"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-22 04:34:20 PM"/>
        <attribute name="created" value="S2t1bGliO0RFU0tUT1AtN0JOTzg4NjsyNTY4LTA3LTE2OzA2OjMzOjMyIFBNOzI5MzM="/>
        <attribute name="edited" value="S2t1bGliO0RFU0tUT1AtN0JOTzg4NjsyNTY4LTA3LTE2OzA2OjQ4OjAxIFBNOzE7MzA0Mw=="/>
        <attribute name="edited" value="TkJPRFRLS1U7TkJPRFQwMDA7MjAyNS0wNy0yMjswNDozNDoyMCBQTTsyOzI1MTU="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, year, i" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; year">
                <assign variable="money" expression="money * (1+interest/100)"/>
                <output expression="&quot;Year &quot; &amp; (i+1) &amp; &quot;:&quot; &amp; money" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>