<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_4"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 07:22:38 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NTQ6NDUgUE07MjU4MQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6MDc6MjMgUE07MTsyNjg0"/>
        <attribute name="edited" value="YWxlemU7QUxJQ0UtMDEyMTsyMDI1LTA3LTE2OzA3OjIyOjM4IFBNOzM7MjUxOQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="mo, ins, ye" type="Real" array="False" size=""/>
            <declare name="total, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="mo"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="ins"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="ye"/>
            <assign variable="i" expression="1"/>
            <while expression="i&lt;=ye">
                <assign variable="mo" expression="mo*(1 + (ins/100))"/>
                <output expression="&quot;Year &quot; &amp; i &amp; &quot;:&quot; &amp;mo" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>